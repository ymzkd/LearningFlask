from flask import Flask
import ghhops_server as hs
import random
import rhino3dm as rh

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

# https://github.com/mcneel/compute.rhino3d/tree/master/src/ghhops-server-py

# コンポーネントに対応しているWebページとか作れたら良いと思ったけどなかなか
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="examples/pointat.png",
    inputs=[
        # hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsInteger("N", "N", "Circle Creation Count"),
    ],
    outputs=[
        hs.HopsCurve("C", "C", "Circles")
    ]
)
def pointat(N):
    circles = []
    distance = 10.0
    for i in range(N):
        cir = rh.Circle(rh.Point3d(distance * random.random(), distance * random.random(), distance * random.random()), random.random())
        circles.append(cir.ToNurbsCurve())
        
    return circles

if __name__ == "__main__":
    app.run(debug=True)
