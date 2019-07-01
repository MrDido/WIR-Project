
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
public class FinalRanked_Searcher {
   
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
		
		 String path ="C:\\\\Users\\\\matte\\\\Documents\\\\GitHub\\\\WIR-Project - Copy\\";
		 //** INSERT PATH OF THE FOLDER WHERE TO READ SHORT INDEX  AND THE PATH TO STORE FINAL RESULTS **
		    
		 String index = path+args[0]; //rename index path
		 String path_short = path+ args[1]; //rename output path
		    
	    
	    IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(index)));
	    IndexSearcher searcher = new IndexSearcher(reader);
	    Analyzer analyzer = new StandardAnalyzer();
	    
	    QueryParser parser = new QueryParser("contents", analyzer);
	    new File(path_short).mkdir();
	    
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
		    PrintWriter writer = new PrintWriter(path_short + "/" +titleID, "UTF-8");
		    doPagingSearch(searcher,query, writer);
		    writer.close();
		    System.out.println();
      
	    }   
	    System.out.println("FINISHED");
	      reader.close();
   }
    
}
