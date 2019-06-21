/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
public class Top_Searcher {
   
	public static void doPagingSearch(IndexSearcher searcher, Query query) throws IOException {

			// Collect enough docs to show 10 pages
			TopDocs results = searcher.search(query, 10);
			ScoreDoc[] hits = results.scoreDocs;
			
			for (int i=0; i < hits.length;i++) {
				Document doc = searcher.doc(hits[i].doc);
				String path = doc.get("path");
				System.out.println((i+1) + ". " + path);

			}		
	}
	
  /** Simple command-line based search demo. */
  public static void main(String[] args) throws Exception {
	    
		String query_string=null;
	    String index = "/Users/herson/Desktop/WIR/index_Marshmello"; 
	    
	    IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(index)));
	    IndexSearcher searcher = new IndexSearcher(reader);
	    Analyzer analyzer = new StandardAnalyzer();
	    
	    QueryParser parser = new QueryParser("contents", analyzer);
	    
	    
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
		    doPagingSearch(searcher,query);
		    System.out.println();
      
	    }   
	    System.out.println("FINISHED");
	      reader.close();
   }
    
}
