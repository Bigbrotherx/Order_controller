import React from "react";
import { useTable } from "react-table";

export default function MyTable(props) {
    const tableData = props.data;
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
    const { getTableBodyProps, headerGroups, rows, prepareRow } =
        useTable({ columns, data: tableData });
    return (
        <div className="container-table">
            <table {...getTableBodyProps()}>
                <thead>
                    {headerGroups.map((headerGroup) => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                            {headerGroup.headers.map((column) => (
                                <th {...column.getHeaderProps()}>{column.render("Header")}</th>
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
    );
}
