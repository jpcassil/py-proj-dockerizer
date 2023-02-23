git init -b main
git add .
git add .env/* -f
git commit -m "Initial Commit"
gh repo create username/docker_image_name --internal --source=. --remote=upstream --push
git remote add origin git@github.com:username/docker_image_name.git
git push -u origin main