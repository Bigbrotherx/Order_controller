import './App.css';
import React from "react";
import {
  RouterProvider,
  Route,
  createRoutesFromElements,
  createBrowserRouter,
} from "react-router-dom";
import HomePage, { homePageLoader } from "./HomePage";

export default function App() {
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route>
        <Route path="/" element={<HomePage />} loader={homePageLoader} />
      </Route>
    )
  );
  return <RouterProvider router={router} />;
}
