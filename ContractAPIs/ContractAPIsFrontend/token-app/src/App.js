import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Login from "./components/pages/Login";

function App() {
  return (
    <div className="container" style={{ width: "55%", marginTop: "100px" }}>
      <h4
        style={{
          textAlign: "center",
          marginBottom: "50px",
          fontStyle: "italic",
          fontWeight: "bold",
        }}
      >
        Token Generation For Contract
      </h4>
      <Login />
    </div>
  );
}

export default App;
