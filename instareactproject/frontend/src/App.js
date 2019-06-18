import React from 'react';
import './App.css';

class SearchComponent extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      items: [],
      query: "",
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    return (
      <div>
        <h3>Search</h3>
        <MediaList items={this.state.items} />
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="new-search">
            Enter a movie or TV-series:
          </label>
          <input
            id="new-search"
            onChange={this.handleChange}
            value={this.state.text}
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
    if (!this.state.text.length) {
      return;
    }
    // TODO: Search query via API and display results
  }
}

class MediaList extends React.Component {
  render() {
    return (
      <ul>
        {this.props.items.map(item => (
          <li key={item.id}>{item.text}</li>
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
