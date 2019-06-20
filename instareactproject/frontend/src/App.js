import React, { Component } from 'react';
import './App.css';
import TitleService from './TitleService';
const titleService = new TitleService();

class SearchComponent extends Component {
  constructor(props) {
    super(props)
    this.state = {
      titles: [],
      numTitles: 0,
      query: "",
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    return (
      <div className="container">
        <div className="container">
          <h3>Search</h3>
          <div className="form-group">
            <form onSubmit={this.handleSubmit}>
              <div className="input-group mb-3">
                <input
                  id="new-search"
                  onChange={this.handleChange}
                  value={this.state.query}
                  className="form-control"
                  placeholder="Enter a movie or series title"
                />
                <div className="input-group-append">
                  <button className="btn btn-outline-secondary" type="submit" id="button-addon2">Search</button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div className="container">
          <MediaList titles={this.state.titles}/>
        </div>
      </div>
    );
  }

  handleChange(e) {
    this.setState({query: e.target.value});
  }

  handleSubmit(e) {
    e.preventDefault();
    if (!this.state.query.length) {
      return;
    }
    titleService.getTitles(this.state.query).then((res) =>
      this.setState(state => ({
        titles: res['Search'],
        numTitles: res['totalResults'],
        query: ''
      }))
    );
  }
}

class MediaList extends Component {
  render() {
    return (
      <ul className="list-unstyled">
        {this.props.titles.map(title => (
          <li className="media my-4" key={title.imdbID}>
            <img src={title.Poster} className="mr-3" alt=""></img>
            <div className="media-body">
              <h5 className="mt-0 mb-1">{title.Title}</h5>
              {title.Year}
              </div>
          </li>
        ))}
      </ul>
    );
  }
}

function App() {
  return (
    <SearchComponent/>
  );
}

export default App;
