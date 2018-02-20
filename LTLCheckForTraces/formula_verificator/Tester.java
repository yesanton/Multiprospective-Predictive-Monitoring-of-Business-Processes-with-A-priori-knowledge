package formula_verificator;

import java.io.File;

import org.deckfour.xes.in.XParser;
import org.deckfour.xes.in.XesXmlGZIPParser;
import org.deckfour.xes.model.XLog;
import org.deckfour.xes.model.XTrace;
import org.processmining.plugins.declareanalyzer.DeclareAnalyzerSingleTracePlugin;
import org.processmining.plugins.declareminer.visualizing.AssignmentModel;
import org.processmining.plugins.declareminer.visualizing.AssignmentViewBroker;
import org.processmining.plugins.declareminer.visualizing.DeclareMap;
import org.processmining.plugins.declareminer.visualizing.XMLBrokerFactory;

public class Tester {

	public static void main(String[] args) throws Exception {
		String logFile = "/media/sf_SharedFolder/BPI_Challenge_2012.xes.gz";
		String modelFile = "/media/sf_SharedFolder/bpi_2012_mined_model.xml";
	
		XParser parser = new XesXmlGZIPParser();
		XLog log = parser.parse(new File(logFile)).get(0);

		DeclareMap model = getModel(modelFile);

		DeclareAnalyzerSingleTracePlugin analysis = new DeclareAnalyzerSingleTracePlugin();
		for (XTrace trace : log) {
			analysis.analyze(trace, model);
		}
	}
	
	private static DeclareMap getModel(String fileName) {
		AssignmentViewBroker broker = XMLBrokerFactory.newAssignmentBroker(fileName);
		AssignmentModel model = broker.readAssignment();
		DeclareMap map = new DeclareMap(model, null, null, null, broker, null);
		return map;
	}

}
