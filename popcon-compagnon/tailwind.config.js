/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "popup-mask": "rgba(0, 0, 0, 0.4)",
      },
    },
  },
  plugins: [],
};
