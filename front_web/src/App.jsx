import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import  Card  from "../components/card";
export const App = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/").then((res) => {
      console.log(res.data);
      setData(res.data);
    });
  }, []);

  return (
    <div>
      {data.length == 0
        ? "no data"
        : data.map((el) => <Card key={el.img} post={el} />)}
    </div>
  );
};

