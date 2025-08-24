import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';

export interface CloudSaverStackProps extends cdk.StackProps {
  envName: string,
  schedule: {
    hour: number,
    minute: number
  }
  email: {
    user: string,
    password: string,
    name: string,
    from: string,
    smtp: string,
    port: number,
    to: Array<string>,
    cc: Array<string>,
    cco: Array<string>,
  },
  format: {
    header: {
      bgColor: string,
      fontColor: string
    },
    body: {
      odd: {
        bgColor: string,
        fontColor: string
      },
      even: {
        bgColor: string,
        fontColor: string
      },
    }
  }
}

export class CloudSaverStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: CloudSaverStackProps) {
    super(scope, id, props);

    const dockerLambda = new lambda.DockerImageFunction(this, "DockerLambda", {
      functionName: `cloudsaver-${props.envName}-lambda`,
      code: lambda.DockerImageCode.fromImageAsset("./image"),
      memorySize: 1024,
      timeout: cdk.Duration.seconds(60),
      architecture: lambda.Architecture.X86_64,
      loggingFormat: lambda.LoggingFormat.JSON,
      environment: {
        // EMAIL
        EMAIL_USER: props.email.user,
        EMAIL_PASSWORD: props.email.password,
        EMAIL_NAME: props.email.name,
        EMAIL_FROM: props.email.from,
        SMTP_ADDRESS: props.email.smtp,
        SMTP_PORT: props.email.port.toString(),
        EMAIL_TO: props.email.to.join(","),
        EMAIL_CC: props.email.cc.join(","),
        EMAIL_CCO: props.email.cco.join(","),

        // FORMAT
        HEADER_BG_COLOR: props.format.header.bgColor,
        HEADER_FONT_COLOR: props.format.header.fontColor,
        BODY_ODD_BG_COLOR: props.format.body.odd.bgColor,
        BODY_ODD_FONT_COLOR: props.format.body.odd.fontColor,
        BODY_EVEN_BG_COLOR: props.format.body.even.bgColor,
        BODY_EVEN_FONT_COLOR: props.format.body.even.fontColor,
      }
    });

    dockerLambda.addToRolePolicy(new iam.PolicyStatement({
      actions: ['ce:GetCostAndUsage'],
      resources: ['*'],
    }));

    new events.Rule(this, 'ScheduleRule', {
      schedule: events.Schedule.cron({
        minute: `${props.schedule.minute}`,
        hour: `${props.schedule.hour}`
      }),
      targets: [new targets.LambdaFunction(dockerLambda)],
    })
  }
}