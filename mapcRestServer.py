from sanic import Sanic
from sanic.response import json
import centralized.cbs.cbs as cbs

app = Sanic(name="myapp")

@app.route('/centralized/cbs',methods=["POST",])
async def test(request):
    print(request)
    env = createEnvFromRequest(request)
    res = cbs.rest_call(env)
    print(res.keys())
    return json(res)
    #
    #
    # res= cbs.main()
    # return json(res)


def createEnvFromRequest(req):
    dimension = list(req.json['dimension'].values())
    obstacles = [tuple(x.values()) for x in req.json['obstacles']]
    agents = [reolveAgent(agent) for agent in req.json['agents']]
    print(dimension)
    print(obstacles)
    print(agents)
    return cbs.Environment(dimension, agents, obstacles)


def reolveAgent(agent):
    return {'start': list(agent['start'].values()), 'goal': list(agent['goal'].values()), 'name': agent['name']}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)