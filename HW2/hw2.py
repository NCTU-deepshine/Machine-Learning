import math

entry = [\
        ["A", 5.5, 0.5, 4.5, 2],\
        ["B", 7.4, 1.1, 3.6, 0],\
        ["C", 5.9, 0.2, 3.4, 2],\
        ["D", 9.9, 0.1, 0.8, 0],\
        ["E", 6.9, -0.1, 0.6, 2],\
        ["F", 6.8, -0.3, 5.1, 2],\
        ["G", 4.1, 0.3, 5.1, 1],\
        ["H", 1.3, -0.2, 1.8, 1],\
        ["I", 4.5, 0.4, 2.0, 0],\
        ["J", 0.5, 0.0, 2.3, 1],\
        ["K", 5.9, -0.1, 4.4, 0],\
        ["L", 9.3, -0.2, 3.2, 0],\
        ["M", 1.0, 0.1, 2.8, 1],\
        ["N", 0.4, 0.1, 4.3, 1],\
        ["O", 2.7, -0.5, 4.2, 1]]

nodes = []
field = []
nodes.append(list(entry))

def euclideanDistance(x1, x2):
    result = 0.0
    for i in xrange(len(x1)):
        result += (x1[i]-x2[i])*(x1[i]-x2[i])
    return math.sqrt(result)

def getNeighbors(X, Z, xt, k):
    input = zip(X, Z)
    input = sorted(input, key=lambda item: euclideanDistance(item[0], xt))
    result = []
    for i in xrange(k):
        result.append((input[i][0], input[i][1], euclideanDistance(input[i][0], xt)))
    return result

def getResponse(neighbors, c=3):
    C = 0.0
    result = 0.0
    for point in neighbors:
        C += 1 / point[2]
        result += point[1] / point[2]
    return result / C

X = []
Z = []
for item in entry:
    X.append([item[1], item[2], item[3]])
    Z.append(item[4])

xt = [4.1, -0.1, 2.2]
print getResponse(getNeighbors(X, Z, xt, 3))
xt = [6.1, -0.4, 1.3]
print getResponse(getNeighbors(X, Z, xt, 3))


def splitNode(node):
    total = [0.0, 0.0, 0.0]
    for item in node:
        total[item[4]] += 1
        points = sum(total)
        root = 1.0
        xValue = 1.0
        xSplit = 0.0
        yValue = 1.0
        ySplit = 0.0
        zValue = 1.0
        zSplit = 0.0
        for x in total:
            root -= (x/points)*(x/points)

        x = sorted(node, key=lambda point: point[1])
        counter = [0.0, 0.0, 0.0]
        for i in xrange(len(x)-1):
            counter[x[i][4]] += 1
        a = 1.0
        b = 1.0
        for j in xrange(3):
            a -= (counter[j]/(i+1))*(counter[j]/(i+1))
            b -= ((total[j] - counter[j])/(points-i-1))*((total[j] - counter[j])/(points-i-1))
        a *= (i+1)/points
        b *= (points-i-1)/points
        if a+b < xValue:
            xValue = a+b
            xSplit = i+1

        y = sorted(node, key=lambda point: point[2])
        counter = [0.0, 0.0, 0.0]
        for i in xrange(len(y)-1):
            counter[y[i][4]] += 1
        a = 1.0
        b = 1.0
        for j in xrange(3):
            a -= (counter[j]/(i+1))*(counter[j]/(i+1))
            b -= ((total[j] - counter[j])/(points-i-1))*((total[j] - counter[j])/(points-i-1))
        a *= (i+1)/points
        b *= (points-i-1)/points
        if a+b < yValue:
            yValue = a+b
            ySplit = i+1
    
        z = sorted(node, key=lambda point: point[3])
        counter = [0.0, 0.0, 0.0]
        for i in xrange(len(z)-1):
            counter[z[i][4]] += 1
        a = 1.0
        b = 1.0
        for j in xrange(3):
            a -= (counter[j]/(i+1))*(counter[j]/(i+1))
            b -= ((total[j] - counter[j])/(points-i-1))*((total[j] - counter[j])/(points-i-1))
        a *= (i+1)/points
        b *= (points-i-1)/points
        if a+b < zValue:
            zValue = a+b
            zSplit = i+1

    if root <= xValue and root <= yValue and root <= zValue:
        nodes.append([])
        nodes.append([]) 
        print "No need to split anymore"
    elif xValue <= yValue and xValue <= zValue:
        nodes.append(x[:xSplit])
        nodes.append(x[xSplit:])
        print "Split at x=", (x[xSplit-1][1]+x[xSplit][1])/2
    elif yValue <= xValue and yValue <= zValue:
        nodes.append(y[:ySplit])
        nodes.append(y[ySplit:])
        print "Split at y=", (y[ySplit-1][1]+y[ySplit][1])/2
    elif zValue <= yValue and zValue <= xValue:
        nodes.append(z[:zSplit])
        nodes.append(z[zSplit:])
        print "Split at z=", (z[zSplit-1][1]+z[zSplit][1])/2

def printNode(node):
    total = [0.0, 0.0, 0.0]
    for item in node:
        total[item[4]] += 1
    points = sum(total)
    if points == 0:
        print "Empty Node!"
        return
    root = 1.0
    for x in total:
        root -= (x/points)*(x/points)
    print "GINI index : ", root
    print "class distribution: ", total

'''splitNode(nodes[0])
splitNode(nodes[1])
splitNode(nodes[2])
print "how many nodes? ",len(nodes)
print "Node 1"
printNode(nodes[0])
print "Node 2"
printNode(nodes[1])
print "Node 3"
printNode(nodes[2])
print "Node 4"
printNode(nodes[3])
print "Node 5"
printNode(nodes[4])
print "Node 6"
printNode(nodes[5])
print "Node 7"
printNode(nodes[6])'''

