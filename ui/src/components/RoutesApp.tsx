import { Route, Routes } from "react-router-dom";
import { Home } from "../pages/Home";
import { SuccesfulIssue } from "../pages/SuccesfulIssue";

export function RoutesApp() {
  return (
    <Routes>
      <Route 
        index
        element={<Home/>}
      />
      <Route 
        path='/succesful_issue'
        element={<SuccesfulIssue/>}
      />
    </Routes>
  )
}