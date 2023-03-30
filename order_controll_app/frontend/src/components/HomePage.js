import React from "react";
import {
  RouterProvider,
  Route,
  createRoutesFromElements,
  createBrowserRouter,
} from "react-router-dom";
import HomePageContent, { homePageLoader } from "./HomePageContent";

export default function HomePage() {
    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route>
                <Route path="/" element={<HomePageContent />} loader={homePageLoader} />
            </Route>
        )
    );
    return (
        <RouterProvider router={router} />
    );
}
