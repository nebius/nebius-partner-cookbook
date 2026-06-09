import { cpSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { join } from "node:path";

const appDir = join(import.meta.dir, "..", "app");
const standaloneAppDir = join(appDir, ".next", "standalone", "app");
const serverPath = join(standaloneAppDir, "server.js");

if (!existsSync(serverPath)) {
  throw new Error(`Next standalone server not found at ${serverPath}. Run the app build first.`);
}

function copyDirectory(source: string, destination: string): void {
  if (!existsSync(source)) {
    throw new Error(`Required deploy asset directory not found: ${source}`);
  }
  rmSync(destination, { force: true, recursive: true });
  mkdirSync(destination, { recursive: true });
  cpSync(source, destination, { recursive: true });
}

copyDirectory(join(appDir, "public"), join(standaloneAppDir, "public"));
copyDirectory(join(appDir, ".next", "static"), join(standaloneAppDir, ".next", "static"));

console.log("Prepared Next standalone deployment assets.");
