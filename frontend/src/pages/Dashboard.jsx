import { useState, useEffect } from "react";
import axios from "axios";

const fetchNotesHistory = async (authToken) => {
  const res = await axios.get("http://127.0.0.1:8000/notes/history", {
    headers: {
      Authorization: `Bearer ${authToken}`,
    },
  });

  return res.data;
};

export default function Dashboard() {
  const [topic, setTopic] = useState("");
  const [notes, setNotes] = useState("");
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  // 🔐 Protect route
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      window.location.href = "/";
      return;
    }

    fetchNotesHistory(token)
      .then(setHistory)
      .catch((err) => {
        console.error(err);
      });
  }, []);

  // 🔥 Generate Notes
  const generateNotes = async () => {
    if (!topic) return alert("Enter a topic");

    const token = localStorage.getItem("token");

    if (!token) {
      window.location.href = "/";
      return;
    }

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/notes/generate",
        { topic },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setNotes(res.data.content);
      const updatedHistory = await fetchNotesHistory(token);
      setHistory(updatedHistory);
      setTopic("");
    } catch (err) {
      console.error(err);
      alert("Error generating notes ❌");
    } finally {
      setLoading(false);
    }
  };

  // 🔓 Logout
  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div className="flex h-screen bg-[#0f172a] text-white">

      {/* 🔹 SIDEBAR */}
      <div className="w-80 bg-[#020617] p-5 border-r border-gray-800 overflow-y-auto">
        
        {/* 🧠 APP NAME */}
        <h1 className="text-2xl font-bold mb-6 text-blue-400">
          Mentora AI 🤖
        </h1>

        <h2 className="text-lg font-semibold mb-4 text-gray-300">
          📚 Your Notes
        </h2>

        {history.length === 0 ? (
          <p className="text-gray-500">No notes yet</p>
        ) : (
          history.map((item) => (
            <div
              key={item.id}
              className="mb-3 p-3 bg-[#0f172a] rounded-lg hover:bg-[#1e293b] cursor-pointer transition"
              onClick={() => setNotes(item.content)}
            >
              <h3 className="font-medium">{item.topic}</h3>
              <p className="text-sm text-gray-400 truncate">
                {item.content}
              </p>
            </div>
          ))
        )}
      </div>

      {/* 🔹 MAIN AREA */}
      <div className="flex-1 flex flex-col">

        {/* 🔥 HEADER */}
        <div className="flex justify-between items-center p-6 border-b border-gray-800">
          <h2 className="text-xl font-semibold text-gray-200">
            AI Study Assistant ✨
          </h2>

          <button
            onClick={handleLogout}
            className="px-4 py-2 bg-red-500 hover:bg-red-600 rounded-lg text-sm"
          >
            Logout
          </button>
        </div>

        {/* 🔹 CONTENT */}
        <div className="p-10 overflow-y-auto flex-1">

          {/* ✍️ INPUT BOX */}
          <div className="bg-[#020617] p-6 rounded-xl shadow-lg mb-6 border border-gray-800">
            <textarea
              placeholder="Ask Mentora AI to generate notes..."
              className="w-full bg-transparent outline-none text-lg resize-none placeholder-gray-500"
              rows={2}
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
            />

            <button
              onClick={generateNotes}
              disabled={loading}
              className="mt-4 px-5 py-2 bg-blue-500 hover:bg-blue-600 rounded-lg font-medium disabled:opacity-50"
            >
              {loading ? "Generating..." : "Generate ✨"}
            </button>
          </div>

          {/* 📄 OUTPUT */}
          <div className="bg-[#020617] p-6 rounded-xl border border-gray-800 shadow-lg min-h-[300px]">
            {notes ? (
              <div className="whitespace-pre-wrap text-gray-200 leading-relaxed">
                {notes}
              </div>
            ) : (
              <p className="text-gray-500">
                Your AI-generated notes will appear here...
              </p>
            )}
          </div>

        </div>
      </div>
    </div>
  );
}