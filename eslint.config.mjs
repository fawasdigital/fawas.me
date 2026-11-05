import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  globalIgnores([
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
    "script.js",
    "fonts/**",
  ]),
  {
    files: [
      "components/hero-scene.tsx",
      "components/work-header-scene.tsx",
      "components/connect-globe.tsx",
    ],
    rules: {
      "react/no-unknown-property": "off",
    },
  },
]);

export default eslintConfig;
