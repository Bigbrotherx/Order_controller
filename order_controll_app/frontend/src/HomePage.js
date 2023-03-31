import React, { useEffect, useState } from "react";
import { useLoaderData } from "react-router-dom";
import MyGraph from "./MyGraph";
import MyTable from "./MyTable";

const BASE_URL = "http://localhost:5000/order-info";

export default function HomePage() {
  const { data } = useLoaderData();
  const [tableData, setTableData] = useState(data);
  const [total, setTotal] = useState(getTotalPrice(data));
  const isDataLoaded = data ? false : true
  const [isOrdersLoadingError, setIsOrdersLoadingError] =
    useState(isDataLoaded);

  useEffect(() => {
    const interval = setInterval(getOrdersData, 60000);
    return function cleanup() {
      clearInterval(interval);
    };
  }, []);

  function getTotalPrice(data) {
    var result = 0;
    if (data) {
      data.forEach((element) => {
        result += element.price_usd;
      });
    }
    return result
  }

  function getOrdersData() {
    fetch(BASE_URL)
      .then((response) => {
        if (!response.ok) {
          setIsOrdersLoadingError(true);
          throw new Error("Ошибка сервера!")
        } else {
          return response.json();
        }
      })
      .then((data) => {
        setTotal(getTotalPrice(data));
        setTableData(data);
      })
      .catch((error) => {
        setIsOrdersLoadingError(true);
        console.error("Ошибка:", error);
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
      {isOrdersLoadingError ?
        <label className="data">Ошибка загрузки заказов</label> :
        <main>
          <div className="data">
            <div>
              <label id="total">Всего, $:</label>
              <textarea id="total" value={total} readOnly={true} />
            </div>
            <MyTable data={tableData} />
          </div>
          <div className="graph">
            <MyGraph data={tableData} />
          </div>
        </main>
      }
    </div>
  );
}

const homePageLoader = async ({ request, params }) => {
  try {
    const response = await fetch(BASE_URL);
    if (!response.ok) {
      throw new Error("Ошибка сервера!");
    } else {
      const data = await response.json();
      return { data };
    }
  } catch (error) {
    {
      console.error("Ошибка:", error);
      return [];
    }
  }
};

export { homePageLoader };
