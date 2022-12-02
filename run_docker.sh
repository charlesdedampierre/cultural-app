
set -e
set -x

echo "*********** STARTING ***********"

PORT=${PORT:-8080}
APP=${APP:-app.py}

streamlit run --server.port $PORT $APP
