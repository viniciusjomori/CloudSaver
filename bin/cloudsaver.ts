import * as cdk from 'aws-cdk-lib';
import { CloudSaverStack } from '../lib/cloudsaver-stack';
import * as fs from 'fs';
import * as path from 'path';

const app = new cdk.App();

let envName = app.node.tryGetContext('env')
const config = getConfig(envName)

new CloudSaverStack(app, 'CloudSaverStack', {
  envName: envName,
  ...config
});

function getConfig(envName: string) {
  const configPath = path.resolve(__dirname, `../env/${envName}.json`);
  
  if (!fs.existsSync(configPath)) throw new Error(`env not found: ${configPath}`);

  const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  return config
}