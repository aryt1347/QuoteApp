import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [quoteData, setQuoteData] = useState("");
  const [authorLink, setAuthorLink] = useState("");

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/get_quote/')
      .then((res) => res.json())
      .then((data) => {
        
        setQuoteData(data)

        // Create and set link to author's bio
        let authorLink = "https://en.wikipedia.org/wiki/" + data.author.split(" ").join("_");
        setAuthorLink(authorLink);
        console.log(data.bio);
      });
  }, []);

  return (
    <>
      <div>
        { quoteData ? ( 
          <>
          <h2>"{quoteData.content}"</h2>
          <a href={authorLink} target='_blank'>- { quoteData.author }</a>
          <p>Topic: { quoteData.topic }</p>
        </>
        ) 
        : (<p> "Loading Quote" </p>)}
      </div>
    </>
  )
}

export default App
