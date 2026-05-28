import { useEffect, useState } from "react";
import { api } from "./api";
import "./index.css";

function App() {
  const [activities, setActivities] = useState([]);
  const [sourceType, setSourceType] = useState("sap");
  const [file, setFile] = useState(null);

  const loadActivities = async () => {
    const res = await api.get("/activities/");
    setActivities(res.data);
  };

  useEffect(() => {
    loadActivities();
  }, []);

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("source_type", sourceType);
    formData.append("file", file);

    await api.post("/upload/", formData);
    setFile(null);
    await loadActivities();
  };

  const approve = async (id) => {
    await api.post(`/activities/${id}/approve/`, {
      comment: "Reviewed by analyst",
    });
    await loadActivities();
  };

  const lock = async (id) => {
    await api.post(`/activities/${id}/lock/`);
    await loadActivities();
  };

  const pending = activities.filter((a) => a.status === "pending").length;
  const suspicious = activities.filter((a) => a.status === "suspicious").length;
  const approved = activities.filter((a) => a.status === "approved").length;
  const locked = activities.filter((a) => a.status === "locked").length;

  return (
    <div className="container">
      <h1 className="title">Breathe ESG Review Dashboard</h1>

      <section className="section">
        <h2>Upload Source File</h2>

        <div className="upload-row">
          <select
            value={sourceType}
            onChange={(e) => setSourceType(e.target.value)}
          >
            <option value="sap">SAP Fuel / Procurement</option>
            <option value="utility">Utility Electricity</option>
            <option value="travel">Corporate Travel</option>
          </select>

          <input
            type="file"
            accept=".csv"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <button onClick={uploadFile} disabled={!file}>
            Upload
          </button>
        </div>
      </section>

      <section className="section">
        <h2>Summary</h2>

        <div className="summary-grid">
          <div className="card">
            <h3>Total</h3>
            <p>{activities.length}</p>
          </div>

          <div className="card">
            <h3>Pending</h3>
            <p>{pending}</p>
          </div>

          <div className="card">
            <h3>Suspicious</h3>
            <p>{suspicious}</p>
          </div>

          <div className="card">
            <h3>Approved</h3>
            <p>{approved}</p>
          </div>

          <div className="card">
            <h3>Locked</h3>
            <p>{locked}</p>
          </div>
        </div>
      </section>

      <section className="section table-section">
        <h2>Review Queue</h2>

        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Scope</th>
                <th>Activity</th>
                <th>Site</th>
                <th>Quantity</th>
                <th>Emissions kgCO2e</th>
                <th>Status</th>
                <th>Flags</th>
                <th>Raw Source</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              {activities.map((a) => (
                <tr key={a.id}>
                  <td>{a.id}</td>
                  <td>{a.scope}</td>
                  <td>{a.activity_type}</td>
                  <td>{a.site_code || "-"}</td>
                  <td>
                    {a.quantity_normalized ?? "-"} {a.unit_normalized}
                  </td>
                  <td>
                    {a.emissions_kgco2e
                      ? Number(a.emissions_kgco2e).toFixed(2)
                      : "-"}
                  </td>
                  <td className={`status-${a.status}`}>{a.status}</td>
                  <td className="flags">
                    <td>
  {a.flags?.length > 0 ? (
    <span className="flags">{a.flags.join(", ")}</span>
  ) : (
    <span style={{ color: "#94a3b8" }}>None</span>
  )}
</td>                  </td>
                  <td>
                    <details>
                      <summary>View</summary>
                      <pre>{JSON.stringify(a.raw_payload, null, 2)}</pre>
                    </details>
                  </td>
                  <td>
                    {a.status !== "locked" && (
                      <button onClick={() => approve(a.id)}>Approve</button>
                    )}

                    {a.status === "approved" && (
                      <button onClick={() => lock(a.id)}>Lock</button>
                    )}

                    {a.status === "locked" && (
                      <span className="locked-text">Locked</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

export default App;