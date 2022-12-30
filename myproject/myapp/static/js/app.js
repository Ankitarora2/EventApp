import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      events: [],
      isLoading: true,
      isLoggedIn: false,
      email: '',
      password: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleLogin = this.handleLogin.bind(this);
    this.handleInterest = this.handleInterest.bind(this);
    this.handleRating = this.handleRating.bind(this);
  }

  componentDidMount() {
    this.getEvents();
  }

  getEvents() {
    fetch('/events/')
      .then(response => response.json())
      .then(data => this.setState({ events: data, isLoading: false }));
  }

  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }

  handleLogin(event) {
    event.preventDefault();
    const data = {
      email: this.state.email,
      password: this.state.password
    };
    fetch('/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          this.setState({ isLoggedIn: true });
        }
      });
  }

  handleInterest(event) {
    event.preventDefault();
    const data = {
      event_id: event.target.value
    };
    fetch('/interest/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
  }

  handleRating(event) {
    event.preventDefault();
    const data = {
      event_id: event.target.name,
      rating: event.target.value
    };
    fetch('/rating/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
  }

  render() {
    if (this.state.isLoading) {
      return <p>Loading...</p>;
    }

    if (!this.state.isLoggedIn) {
      return (
        <form onSubmit={this.handleLogin}>
          <label>
            Email:
            <input
              type="text"
              name="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </label>
          <br />
          <label>
            Password:
            <input
              type="password"
              name="password
