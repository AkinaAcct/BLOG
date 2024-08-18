import sys
import pypandoc

filepath = sys.argv[1]
outputpath = sys.argv[2]

pypandoc.convert_file(filepath, "md", "epub", outputfile=outputpath)
