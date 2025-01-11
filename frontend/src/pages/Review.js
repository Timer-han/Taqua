import { React, useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getSuggests } from "../services/api";
import SuggestCard from "../components/SuggestCard";
import "../css/Review.css"

const Review = () => {
    const [suggests, setSuggests] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadSuggestedQuestions = async () => {
            try {
                const suggests = await getSuggests();
                setSuggests(suggests);
            } catch (err) {
                console.log(err);
                setError("Ошибка загрузки, обратись в поддержку")
            } finally {
                setLoading(false);
            }
        };

        loadSuggestedQuestions();
    }, [])

    return (
        <div className="review">  
        {error && <div className="error-message">{error}</div>}
        {loading ? (
          <div className="loading">Loading...</div>
        ) : (
          <div className="suggests-grid">
            {suggests.map((suggest) => (
              <Link className="suggests-link" to={`/review/${suggest.uuid}`}>
                <SuggestCard suggest={suggest} key={suggest.uuid} />
              </Link>
            ))}
          </div>
        )}
      </div>
    );
}

export default Review;