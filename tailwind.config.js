/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./templates/*.html"],
  theme: {
    extend: {
      fontFamily: {
        'roboto-mono': ['"Roboto Mono"', 'monospace'],
      },
      colors: {
        'primary': '#1a1b1f'
      }
    },
  },
  plugins: [],
}

