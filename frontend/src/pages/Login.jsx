import { useState } from "react";
import axios from "axios";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!email || !password) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/auth/login",
        new URLSearchParams({
          username: email, // OAuth expects username
          password: password,
        }),
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      const token = response.data.access_token;

      // ✅ Save token
      localStorage.setItem("token", token);

      // ✅ Redirect
      window.location.href = "/dashboard";
    } catch (error) {
      console.error(error);
      alert("Invalid email or password ❌");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-[#0f172a] text-white">
      <form
        onSubmit={handleLogin}
        className="w-96 p-8 bg-[#020617] rounded-xl border border-gray-800 shadow-lg"
      >
        {/* 🔥 Title */}
        <h2 className="mb-6 text-2xl text-center font-semibold">
          Welcome Back 👋
        </h2>

        {/* 📧 Email */}
        <input
          type="email"
          placeholder="Email"
          className="w-full p-3 mb-4 bg-gray-800 rounded outline-none focus:ring-2 focus:ring-blue-500"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        {/* 🔑 Password */}
        <input
          type="password"
          placeholder="Password"
          className="w-full p-3 mb-4 bg-gray-800 rounded outline-none focus:ring-2 focus:ring-blue-500"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        {/* 🚀 Button */}
        <button
          disabled={loading}
          className="w-full p-3 bg-blue-500 rounded hover:bg-blue-600 transition disabled:opacity-50"
        >
          {loading ? "Logging in..." : "Login"}
        </button>

        {/* 🔁 Switch to Signup */}
        <p className="text-sm text-center mt-4 text-gray-400">
          Don’t have an account?{" "}
          <span
            className="text-blue-400 cursor-pointer hover:underline"
            onClick={() => (window.location.href = "/signup")}
          >
            Sign up
          </span>
        </p>
      </form>
    </div>
  );
}