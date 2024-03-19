from flask import Flask, render_template, request
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # POSTリクエストの場合は地図を作成
    if request.method == 'POST':
        latitudes = request.form.getlist('latitude')  # 緯度のリスト
        longitudes = request.form.getlist('longitude')  # 経度のリスト
        # 文字列のリストをfloatのリストに変換
        locations = list(zip(map(float, latitudes), map(float, longitudes)))
        
        # 地図を作成
        map = folium.Map(location=[35.6895, 139.6917], zoom_start=5)
        HeatMap(locations).add_to(map)
        
        # 地図をHTMLとして保存し、そのパスをテンプレートに渡す
        map.save('static/heatmap.html')
        return render_template('index.html', heatmap='/static/heatmap.html')

    # GETリクエスト時には空のフォームを表示
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
