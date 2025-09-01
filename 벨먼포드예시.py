# 1. 간선 정보 설정 (시작, 도착, 가중치) = (u,v,w)
# edges = [...] / 간선 정보를 (u,v,w)형태로 저장
edges = [
    (1, 2, 4),
    (1, 3, 5),
    (2, 4, -2),
    (3, 4, 3)
]

# 2. 정점 수와 출발점 설정
V = 4
start = 1

# 3. 거리 리스트 초기화 (무한대로), 시작점은 0
# dist = [...] / 각 노드까지의 최단거리 저장용 리스트
# dist[start] = 0 / 시작점의 거리는 0으로 설정
dist = [float('inf')] * (V + 1) # float('inf') = 양의 무한대 
dist[start] = 0

# 4. (정점 수 - 1)번 간선 전체 확인
#for i in range(V – 1) / (정점 수-1)만큼 반복
for i in range(V - 1):
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

# 5. 음수 사이클 확인
# if dist[v] > dist[u] + w / 더 짧은 경로 발견 시 갱신 
# negative_cycle / 음수 사이클이 있는지 여부 저장하는 변수
negative_cycle = False
for u, v, w in edges:
    if dist[u] != float('inf') and dist[v] > dist[u] + w:
        negative_cycle = True
        break

# 6. 결과 출력
if negative_cycle:
    print("음수 사이클이 존재합니다.")
else:
    for i in range(1, V + 1):
        print(f"{start} → {i} 최단 거리: {dist[i]}")


