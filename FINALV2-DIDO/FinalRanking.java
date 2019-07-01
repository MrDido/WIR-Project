/**BEFORE COMPILING CHANGE VARIABALE "path" **/
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.BooleanQuery;

/** Simple command-line based search demo. */
public class FinalRanking {
   
	public static void doPagingSearch(IndexSearcher searcher, Query query, PrintWriter writer) throws IOException {
			TopDocs results = searcher.search(query, 10);
			ScoreDoc[] hits = results.scoreDocs;
			
			for (int i=0; i < hits.length;i++) {
				Document doc = searcher.doc(hits[i].doc);
				String path = doc.get("path");
				writer.println(doc.get("title").replace(".txt", ""));
				System.out.println((i+1) + ". " + path + "||SCORE = " + hits[i].score);

			}		
	}
	
  /** Simple command-line based search demo. */
  public static void main(String[] args) throws Exception {
	    
		String query_string=null;
		
		String path ="C:\\Users\\Herson\\Desktop\\WIR\\";
		/** INSERT PATH OF THE FOLDER THAT WILL CONTAIN ALL THE FILES AND JAVA CLASSES **/
		String title = args[0];
		path = path + title;
		
		String short_index = path + "\\Short_Index_" + title; //short index path
		String final_rank = path + "\\FinalRank_" + title; ; //final ranked output path
		    
	    
	    IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(short_index)));
	    IndexSearcher searcher = new IndexSearcher(reader);
	    Analyzer analyzer = new StandardAnalyzer();
	    
	    QueryParser parser = new QueryParser("contents", analyzer);
	    new File(final_rank).mkdir();
	    
	    for(int i = 0; i < reader.numDocs();i++) {
	    	Document doc = reader.document(i);
	        String titleID = doc.get("title");
	        if(titleID.equals(".DS_Store")|| titleID.equals(".txt"))
	        	continue;
	        System.out.println(titleID);
	        String contenuto = doc.get("contents").toString();
	        query_string = contenuto;
	        if(query_string.equals("")) continue;
	        BooleanQuery.setMaxClauseCount( Integer.MAX_VALUE );
	        Query query = parser.parse(query_string);   
		    System.out.println("Searching for: " + query.toString("contents"));
		    PrintWriter writer = new PrintWriter(final_rank + "/" +titleID, "UTF-8");
		    doPagingSearch(searcher,query, writer);
		    writer.close();
		    System.out.println();
      
	    }   
	    System.out.println("FINISHED");
	      reader.close();
   }
    
}
