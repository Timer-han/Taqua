import React from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar"
import AddQuestion from "./pages/AddQuestion";
import Review from "./pages/Review"

function App() {
  return (
    <>
      <NavBar />
      <main>
        <Routes>
          <Route path="/" element={<AddQuestion />} />
          <Route path="/review" element={<Review />} />
        </Routes>
      </main>
    </>
  );
}

export default App;
