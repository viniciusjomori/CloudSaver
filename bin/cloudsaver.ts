import * as cdk from 'aws-cdk-lib';
import { CloudSaverStack } from '../lib/cloudsaver-stack';

const app = new cdk.App();
new CloudSaverStack(app, 'CloudSaverStack', {
  
});