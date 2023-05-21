/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    container: {
      center: true,
    },
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'white': '#ffffff',
      'lime': {
          '50': '#e7ffe4',
          '100': '#c9ffc4',
          '200': '#98ff90',
          '300': '#56ff50',
          '400': '#00ff00',
          '500': '#00e606',
          '600': '#00b809',
          '700': '#008b07',
          '800': '#076d0d',
          '900': '#0b5c11',
          '950': '#003406',
      },
      // ...
    },
  },
  plugins: [],
}
