import { useState, useEffect } from 'react'
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  const [quoteData, setQuoteData] = useState("");
  const [authorLink, setAuthorLink] = useState("");
  const [showBio, setShowBio] = useState(false);
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/get_quote/')
      .then((res) => res.json())
      .then((data) => {
        setQuoteData(data)
        // Set link to author's bio
        let authorLink = "https://en.wikipedia.org/wiki/" + data.author.split(" ").join("_");
        setAuthorLink(authorLink);
        console.log(data.bio);
      });
  }, []);

  function handleShowBio(){
    setShowBio(!showBio);
  }

  return (
    <>
      <div>
        { (quoteData) ? ( 
          <>
          <h2>"{quoteData.content}"</h2>
          <a href={authorLink} target='_blank'>- { quoteData.author }</a>
          <p>Topic: { quoteData.topic }</p>
          <Button variant="primary" onClick={handleShowBio}>
            {showBio ? ("Hide Bio") : ("Show Author's Bio") }
          </Button>
          <div style={{ width: '50%', display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            textAlign: 'center',
            margin: '0 auto'}}>
            { showBio && (
              quoteData.bio
            )}
          </div>
       
        </>
        ) 
        : (
          <Spinner animation="border" />      
      )}
      </div>
    </>
  )
}

export default App
