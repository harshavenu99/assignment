plan-dev:
	DEPLOY_ENVIRONMENT=dev CI=1 pipenv run runway plan
deploy-dev:
	DEPLOY_ENVIRONMENT=dev CI=1 pipenv run runway deploy
destroy-dev:
	DEPLOY_ENVIRONMENT=dev CI=1 pipenv run runway destroy