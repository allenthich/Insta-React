import React, { Component } from 'react';
import './App.css';
import TitleService from './TitleService';
const titleService = new TitleService();

class SearchComponent extends Component {
  constructor(props) {
    super(props)
    this.state = {
      query: "",
      titles: [],
      numTitles: 0,
      dateDescending: true,
    }
    this.handleQueryChange = this.handleQueryChange.bind(this);
    this.handleSelectChange = this.handleSelectChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  sortByDateAsc() {
    if (!this.state.dateDescending)
      return
    // TODO: Reverse in place vs. other sort methods
    this.state.titles.sort((a, b) => (new Date(a.first_air_date) - new Date(b.first_air_date)))
    this.setState({dateDescending: false});
  }

  sortByDateDesc() {
    if (this.state.dateDescending)
      return
    // TODO: Reverse in place vs. other sort methods
    this.state.titles.sort((a, b) => (new Date(b.first_air_date) - new Date(a.first_air_date)))
    this.setState({dateDescending: true});
  }

  render() {
    return (
      <div className="container">
        <nav className="navbar navbar-dark bg-dark">
          <form onSubmit={this.handleSubmit} className="form-inline">
            <input 
              className="form-control mr-sm-2" 
              type="search" 
              placeholder="Enter a TV series title" 
              aria-label="Search"
              id="new-search"
              onChange={this.handleQueryChange}
              value={this.state.query}
            />
            <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
          <img 
            alt="https://www.themoviedb.org/assets/2/v4/logos/408x161-powered-by-rectangle-blue-10d3d41d2a0af9ebcb85f7fb62ffb6671c15ae8ea9bc82a2c6941f223143409e.png"
            src="https://www.themoviedb.org/assets/2/v4/logos/408x161-powered-by-rectangle-green-bb4301c10ddc749b4e79463811a68afebeae66ef43d17bcfd8ff0e60ded7ce99.png"
            height="50"
         />
        </nav>
        <div className="container">
          <div className="input-group mb-3">
            <div className="input-group-prepend">
              <label className="input-group-text">Sort:</label>
            </div>
            <select value={this.state.dateDescending} className="custom-select" onChange={this.handleSelectChange}>
              <option value="true">Date Descending</option>
              <option value="false">Date Ascending</option>
            </select>
          </div>
          <MediaList titles={this.state.titles}/>
        </div>
      </div>
    );
  }

  handleQueryChange(e) {
    this.setState({query: e.target.value});
  }

  handleSelectChange(e) {
    if (e.target.value === "true") {
      this.sortByDateDesc()
    } else {
      this.sortByDateAsc()
    }
  }

  handleSubmit(e) {
    e.preventDefault();
    if (!this.state.query.length) {
      return;
    }
    titleService.getTitles(this.state.query).then((res) =>
      this.setState(prevState => ({
        titles: res['results']
          .sort((a, b) => (new Date(b.first_air_date) - new Date(a.first_air_date))),
        numTitles: res['total_results'],
        query: '',
        dateDescending: true
      }))
    );
  }
}

class MediaList extends Component {
  render() {
    return (
        <ul className="list-unstyled">
        {this.props.titles.map(title => (
          <li className="media my-4 li-height-200" id={title.id} key={title.id}>
            <img src={'https://image.tmdb.org/t/p/w500' + title.poster_path} className="mr-3 object-fit-cover" alt=""></img>
            <div className="media-body">
              <h5 className="mt-0 mb-1">{title.name}</h5>
              {title.overview}
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
