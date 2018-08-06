package tutorial;

import java.util.Iterator;
import java.util.function.Supplier;

import org.jgrapht.Graph;
import org.jgrapht.generate.CompleteGraphGenerator;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.SimpleGraph;
import org.jgrapht.traverse.DepthFirstIterator;
import org.jgrapht.util.SupplierUtil;


public class Tutorial {

	public static Graph<String, DefaultEdge> createStringGraph() {
		Graph<String, DefaultEdge> g = new SimpleGraph<>(DefaultEdge.class);

		String v1 = "v1";
		String v2 = "v2";
		String v3 = "v3";
		String v4 = "v4";

		// add the vertices
		g.addVertex(v1);
		g.addVertex(v2);
		g.addVertex(v3);
		g.addVertex(v4);

		// add edges to create a circuit
		g.addEdge(v1, v2);
		g.addEdge(v2, v3);
		g.addEdge(v3, v4);
		g.addEdge(v4, v1);

		return g;
	}


	public static void exemploGrafoCompleto() {
		//Copiado de https://github.com/jgrapht/jgrapht/blob/master/jgrapht-demo/src/main/java/org/jgrapht/demo/CompleteGraphDemo.java

		// number of vertices
		int SIZE = 10;

		// Create the VertexFactory so the generator can create vertices
		Supplier<String> vSupplier = new Supplier<String>()
		{
			private int id = 0;

			@Override
			public String get()
			{
				return "v" + id++;
			}
		};

		Graph<String, DefaultEdge> completeGraph = 
				new SimpleGraph<>(vSupplier,
								  SupplierUtil.createDefaultEdgeSupplier(),
								  false
				);

		// Create the CompleteGraphGenerator object
		CompleteGraphGenerator<String, DefaultEdge> completeGenerator =
				new CompleteGraphGenerator<>(SIZE);


		// Use the CompleteGraphGenerator object to make completeGraph a
		// complete graph with [size] number of vertices
		completeGenerator.generateGraph(completeGraph);
		//@example:generate:end

		// Print out the graph to be sure it's really complete
		Iterator<String> iter = new DepthFirstIterator<>(completeGraph);
		while (iter.hasNext()) {
			String vertex = iter.next();
			System.out.println(
					"Vertex " + vertex + " is connected to: "
							+ completeGraph.edgesOf(vertex).toString());
		}
	}

	public static void main(String[] args) {

		Graph<String, DefaultEdge> grafo = createStringGraph();
		System.out.println(grafo);

		System.out.println("\nExemplor de grafo completo.");
		exemploGrafoCompleto();
		

	}

}
