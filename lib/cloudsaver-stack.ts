import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";

export interface CloudSaverStackProps extends cdk.StackProps {
}

export class CloudSaverStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: CloudSaverStackProps) {
    super(scope, id, props);

  }
}