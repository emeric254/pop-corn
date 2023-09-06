/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "popup-mask": "rgba(0, 0, 0, 0.2)",
        "popcon-blue": "rgb(86, 85, 159)",
        "popcon-orange": "rgb(238, 129, 57)",
        "popcon-green": "rgb(124, 181, 75)",
      },
    },
  },
  plugins: [],
};
