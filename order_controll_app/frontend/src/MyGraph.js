import React from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function MyGraph(props) {
  const data = props.data
  return (
    <ResponsiveContainer width="85%" height={300}>
      <AreaChart
        width={500}
        height={300}
        data={data}
        margin={{
          top: 10,
          right: 30,
          left: 0,
          bottom: 0,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis tick={{ fill: "white" }} dataKey="expires_in" />
        <YAxis tick={{ fill: "white" }} />
        <Tooltip />
        <Area
          type="monotone"
          dataKey="price_usd"
          stroke="#92EA80"
          fill="#92EA80"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}
