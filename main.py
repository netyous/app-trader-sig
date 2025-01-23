import { useState, useEffect } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine } from 'recharts'
import { Card, CardContent, CardHeader, CardTitle } from "/components/ui/card"
import { Button } from "/components/ui/button"
import { Heart, Clock, Users, Play, Home, Search, Menu, User, Settings, Mail, Bell, Calendar, Star, Upload, Download, Trash, Edit, Plus, Minus, Check, X, ArrowRight } from "lucide-react"

type NewsItem = {
  title: string
  description: string
  impact: 'High' | 'Medium' | 'Low'
}

const mockNews: NewsItem[] = [
  { title: 'US GDP Growth Surpasses Expectations', description: 'The US GDP grew by 2.3% in Q4, surpassing expectations.', impact: 'High' },
  { title: 'Fed Announces Interest Rate Hike', description: 'The Federal Reserve has announced a 0.25% interest rate hike.', impact: 'High' },
  { title: 'Economic Calendar Update', description: 'Upcoming economic events include the Non-Farm Payroll report.', impact: 'Medium' },
  { title: 'Tech Sector Update', description: 'Tech stocks are showing signs of recovery.', impact: 'Low' },
]

const mockChartData = [
  { name: '1', uv: 4000, pv: 2400, amt: 2400, rsi: 50, macd: 10, sma: 3000, ema: 3100 },
  { name: '2', uv: 3000, pv: 1398, amt: 2210, rsi: 45, macd: 8, sma: 2900, ema: 2950 },
  { name: '3', uv: 2000, pv: 9800, amt: 2290, rsi: 40, macd: 6, sma: 2800, ema: 2850 },
  { name: '4', uv: 2780, pv: 3908, amt: 2000, rsi: 35, macd: 4, sma: 2700, ema: 2750 },
  { name: '5', uv: 1890, pv: 4800, amt: 2181, rsi: 30, macd: 2, sma: 2600, ema: 2650 },
  { name: '6', uv: 2390, pv: 3800, amt: 2500, rsi: 25, macd: 0, sma: 2500, ema: 2550 },
  { name: '7', uv: 3490, pv: 4300, amt: 2100, rsi: 20, macd: -2, sma: 2400, ema: 2450 },
  { name: '8', uv: 4390, pv: 4300, amt: 2100, rsi: 15, macd: -4, sma: 2300, ema: 2350 },
  { name: '9', uv: 5390, pv: 4300, amt: 2100, rsi: 10, macd: -6, sma: 2200, ema: 2250 },
  { name: '10', uv: 6390, pv: 4300, amt: 2100, rsi: 5, macd: -8, sma: 2100, ema: 2150 },
]

const calculateFibonacciRetracement = (data: any[]) => {
  const high = Math.max(...data.map(d => d.uv))
  const low = Math.min(...data.map(d => d.uv))
  const diff = high - low

  const levels = [
    { label: '0.0', value: high },
    { label: '0.236', value: high - diff * 0.236 },
    { label: '0.382', value: high - diff * 0.382 },
    { label: '0.5', value: high - diff * 0.5 },
    { label: '0.618', value: high - diff * 0.618 },
    { label: '0.786', value: high - diff * 0.786 },
    { label: '1.0', value: low },
  ]

  return levels
}

export default function TradingDashboard() {
  const [news, setNews] = useState<NewsItem[]>(mockNews)
  const [chartData, setChartData] = useState(mockChartData)
  const [fibonacciLevels, setFibonacciLevels] = useState<{ label: string, value: number }[]>([])

  useEffect(() => {
    // Simulate fetching news and chart data
    const fetchNews = async () => {
      // Fetch news from an API
      // For now, we'll use the mock data
    }

    const fetchChartData = async () => {
      // Fetch chart data from an API
      // For now, we'll use the mock data
    }

    fetchNews()
    fetchChartData()

    // Calculate Fibonacci Retracement levels
    const levels = calculateFibonacciRetracement(mockChartData)
    setFibonacciLevels(levels)
  }, [])

  return (
    <div className="p-4">
      <div className="flex justify-between items-center mb-4">
        <CardTitle className="text-2xl font-bold">Trading Dashboard</CardTitle>
        <div className="flex space-x-2">
          <Button variant="outline">
            <Home className="mr-2" />
            Home
          </Button>
          <Button variant="outline">
            <Bell className="mr-2" />
            Notifications
          </Button>
          <Button variant="outline">
            <Settings className="mr-2" />
            Settings
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card className="col-span-1">
          <CardHeader>
            <CardTitle>Live Chart</CardTitle>
          </CardHeader>
          <CardContent>
            <LineChart
              width={500}
              height={300}
              data={chartData}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="uv" stroke="#8884d8" activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="rsi" stroke="#82ca9d" />
              <Line type="monotone" dataKey="macd" stroke="#ffc658" />
              <Line type="monotone" dataKey="sma" stroke="#ff7300" />
              <Line type="monotone" dataKey="ema" stroke="#0088fe" />
              {fibonacciLevels.map((level, index) => (
                <ReferenceLine key={index} y={level.value} label={level.label} stroke="gray" strokeDasharray="3 3" />
              ))}
            </LineChart>
          </CardContent>
        </Card>

        <Card className="col-span-1">
          <CardHeader>
            <CardTitle>News Feed</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {news.map((item, index) => (
              <div key={index} className="p-4 rounded-lg bg-gray-100">
                <h3 className="font-semibold">{item.title}</h3>
                <p className="mt-1 text-gray-600">{item.description}</p>
                <p className="mt-1 text-sm text-gray-500">
                  Impact: <span className={`font-semibold ${item.impact === 'High' ? 'text-red-500' : item.impact === 'Medium' ? 'text-yellow-500' : 'text-green-500'}`}>{item.impact}</span>
                </p>
              </div>
            ))}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
