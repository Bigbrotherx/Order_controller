import React, { useEffect, useState } from "react";
import { useLoaderData } from "react-router-dom";
import MyGraph from "./MyGraph";
import { useTable } from "react-table";

export default function HomePageContent() {
  const { data } = useLoaderData();

  const [tableData, setTableData] = useState(data);
  const [total, setTotal] = useState(getTotalPrice(data));

  useEffect(() => {
    const interval = setInterval(getBackendData, 60000);
    return function cleanup() {
      clearInterval(interval);
    };
  }, []);

  const columns = React.useMemo(
    () => [
      { Header: "№", accessor: "id" },
      { Header: "Заказ №", accessor: "order_name" },
      { Header: "Стоимость, $", accessor: "price_usd" },
      { Header: "Стоимость, Руб", accessor: "price_rub" },
      { Header: "Срок поставки", accessor: "expires_in" },
    ],
    []
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns, data: tableData });

  function getTotalPrice(data) {
    var result = 0;
    data.forEach((element) => {
      result += element.price_usd;
    });
    return result
  }

  function getBackendData() {
    fetch("http://localhost:5000/order-info")
      .then((response) => {
        if (!response.ok) {
          return {};
        } else {
          return response.json();
        }
      })
      .then((data) => {
        setTotal(getTotalPrice(data));
        setTableData(data);
      });
  }

  return (
    <div className="app">
      <header>
        <div className="app-header">
          <div className="icon-box" />
          <h1>Визуализатор заказов</h1>
        </div>
      </header>
      <main>
        <div className="data">
          <div>
            <label id="total">Всего, $:</label>
            <textarea id="total" value={total} readOnly={true} />
          </div>
          <div className="container-table">
            <table {...getTableBodyProps()}>
              <thead>
                {headerGroups.map((headerGroup) => (
                  <tr {...headerGroup.getHeaderGroupProps()}>
                    {headerGroup.headers.map((column) => (
                      <th {...column.getHeaderProps()}>
                        {column.render("Header")}
                      </th>
                    ))}
                  </tr>
                ))}
              </thead>
              <tbody {...getTableBodyProps}>
                {rows.map((row) => {
                  prepareRow(row);
                  return (
                    <tr {...row.getRowProps()}>
                      {row.cells.map((cell) => (
                        <td {...cell.getCellProps()}>{cell.render("Cell")}</td>
                      ))}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
        <div className="graph">
          <MyGraph data={tableData} />
        </div>
      </main>
    </div>
  );
}

const homePageLoader = async ({ request, params }) => {
  const response = await fetch("http://localhost:5000/order-info");
  const data = await response.json();
  return { data };
};

export { homePageLoader };
