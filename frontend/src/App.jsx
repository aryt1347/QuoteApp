import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [quoteData, setQuoteData] = useState("");

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/get_quote/')
      .then((res) => res.json())
      .then((data) => {setQuoteData(data)});
  }, []);

  return (
    <>
      <div>
        { quoteData ? ( 
          <>
          <h2>"{quoteData.content}"</h2>
          <p>- { quoteData.author }</p>
          <p>Topic: { quoteData.topic }</p>
        </>
        ) 
        : (<p> "Loaading Quote" </p>)}
      </div>
    </>
  )
}

export default App
