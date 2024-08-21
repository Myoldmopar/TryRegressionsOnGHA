#include <fstream>
#include <iostream>

int main()
{
    std::cout << "Hello, World!" << std::endl;
    std::ofstream MyFile("eplusout.txt");
    MyFile << "E+ Output";
    MyFile.close();
    return 0;
}

/*
 * OK so we want to make a C++ executable that produces output files
 * We should have a single ctest that knows how to execute the binary
 * The output files should live in build_folder/testfiles
 * That's pretty much all cmake/ctest should know how to do
 * Then in our GitHub Action Workflow file, we should checkout
 *  the current state of the baseline branch, and get the SHA
 * If that SHA+platform happens to exist in the cache, we should grab it from
 *  the cache and extract it into clone_baseline/build/testfiles
 * If it doesn't, then we should make the build folder, build it, and run it.
 * Either way, now we have baseline testfiles/ results ready to go.
 * And either way, we build the current branch and run tests to get mod results.
 * We can now run the regression script and check for diffs
 *  Not sure about reporting...do we still use the dashboard?
 * OK, once done, do one more check to see if this SHA+platform is in the cache
 *  If it is, we're done.  If not, add it to the cache.
 * Assuming this works, we can eliminate:
 *  Our fork of Decent CI
 *  Our fork of the build results repo
 *  Our custom dashboard
 *  Ruby entirely.
 *  My maintenance burden of the CI machines
 *  The CI machines themselves
*/
