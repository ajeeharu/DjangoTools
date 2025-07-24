/** @type {import('tailwindcss').Config} */
module.exports = {
	mode: "jit",
	content: [
		"./input/**/*.{html,js}",
		"./**/*.html",
	],
	theme: {
		extend: {
		},
	},
	variants: {
		extend: {},
		inset: ['even', 'odd'],
	},
	plugins: [],
};

