import React, { Component } from 'react';
import './App.css';
import TitleService from './TitleService';
const titleService = new TitleService();

class SearchComponent extends Component {
  constructor(props) {
    super(props)
    this.state = {
      title: {},
      query: "",
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    return (
      <div>
        <h3>Search</h3>
        <MediaList title={this.state.title}/>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="new-search">
            Enter a movie or TV-series:
          </label>
          <input
            id="new-search"
            onChange={this.handleChange}
            value={this.state.query}
          />
          <button>Search</button>
        </form>
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
    titleService.getTitle(this.state.query).then((res) =>
      this.setState(state => ({
        title: res,
        query: ''
      }))
    );
  }
}

class MediaList extends Component {
  render() {
    return (
      <div>
        <img src={this.props.title.Poster} alt=""></img>
        <div>{this.props.title.Title}</div>
      </div>
    );
  }
}

function App() {
  return (
    <SearchComponent/>
  );
}

export default App;
