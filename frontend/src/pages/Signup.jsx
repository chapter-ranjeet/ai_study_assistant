import { useState } from "react";
import axios from "axios";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:8000/auth/signup", {
        email,
        password,
      });

      alert("Signup successful ✅");
      window.location.href = "/";
    } catch (err) {
      console.error(err);
      alert("Signup failed ❌");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-[#0f172a] text-white">
      <form
        onSubmit={handleSignup}
        className="bg-[#020617] p-8 rounded-xl w-96 border border-gray-800"
      >
        <h2 className="text-2xl mb-6 text-center">Create Account ✨</h2>

        <input
          type="email"
          placeholder="Email"
          className="w-full p-3 mb-4 bg-gray-800 rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-3 mb-4 bg-gray-800 rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="w-full bg-green-500 py-2 rounded hover:bg-green-600">
          Sign Up
        </button>

        {/* 🔁 Switch to Login */}
        <p className="text-sm text-center mt-4 text-gray-400">
          Already have an account?{" "}
          <span
            className="text-green-400 cursor-pointer"
            onClick={() => (window.location.href = "/")}
          >
            Login
          </span>
        </p>
      </form>
    </div>
  );
}