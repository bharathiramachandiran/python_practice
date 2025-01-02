
#!/bin/bash
# Accept the environment argument
arg=$1
echo $arg
# Source the environment variables from the given file
source ./$arg.sh
# Deploy the infrastructure stack
sam deploy \
    -t backendpipeline.yaml \
    --stack-name "${Environment}-${ResourcePrefix}-Backend" \
    --region "${REGION}" \
    --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
    --parameter-overrides \
        "Environment=${Environment}" \
        "ResourcePrefix=${ResourcePrefix}" \
        "StackName=${ResourcePrefix}-backend-resources" \
        "MainGitBranch=${MainGitBranch}" \
        "BackendRepoName=${BackendRepoName}" \
        "Region=${REGION}" \
        "PipelineArtifactBucket=${Environment}-${ResourcePrefix}-artifacts" \
        "Tags=${Tags}" \
        "MainGitBranch=${MainGitBranch}" \
        "CodeStarConnectionArn=${CodeStarConnectionArn}" \
        "SourceCodeProvider=CodeStarSourceConnection" \

echo "All deployments were successful!"