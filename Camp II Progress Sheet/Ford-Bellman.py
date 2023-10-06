import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        List<Edge> graph = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int u = scanner.nextInt() - 1;
            int v = scanner.nextInt() - 1;
            int w = scanner.nextInt();
            graph.add(new Edge(u, v, w));
        }

        int[] result = bellmanFord(graph, n);
        for (int distance : result) {
            System.out.print(distance + " ");
        }
    }

    static class Edge {
        int u;
        int v;
        int w;

        public Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }

    static int[] bellmanFord(List<Edge> graph, int n) {
        int[] distances = new int[n];
        Arrays.fill(distances, 30000);
        distances[0] = 0;

        for (int i = 0; i < n - 1; i++) {
            for (Edge edge : graph) {
                int u = edge.u;
                int v = edge.v;
                int w = edge.w;
                if (distances[u] != 30000) {
                    distances[v] = Math.min(distances[v], distances[u] + w);
                }
            }
        }

        return distances;
    }
}
