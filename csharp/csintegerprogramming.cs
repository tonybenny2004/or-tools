// Copyright 2010-2011 Google
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

using System;
using Google.OrTools.LinearSolver;

public class CsIntegerProgramming
{
  private static void RunIntegerProgrammingExample(String solverType)
  {
    MPSolver solver = MPSolver.CreateSolver("IntegerProgramming", solverType);
    if (solver == null)
    {
      Console.WriteLine("Could not create solver " + solverType);
      return;
    }
    double infinity = MPSolver.Infinity();
    // x1 and x2 are integer non-negative variables.
    MPVariable x1 = solver.MakeIntVar(0.0, infinity, "x1");
    MPVariable x2 = solver.MakeIntVar(0.0, infinity, "x2");

    // Minimize x1 + 2 * x2.
    solver.SetObjectiveCoefficient(x1, 1);
    solver.SetObjectiveCoefficient(x2, 2);

    // 2 * x2 + 3 * x1 >= 17.
    MPConstraint ct = solver.MakeConstraint(17, infinity);
    ct.SetCoefficient(x1, 3);
    ct.SetCoefficient(x2, 2);

    int resultStatus = solver.Solve();

    // Check that the problem has an optimal solution.
    if (resultStatus != MPSolver.OPTIMAL)
    {
      Console.WriteLine("The problem does not have an optimal solution!");
      return;
    }

    Console.WriteLine("Problem solved in " + solver.WallTime() +
                       " milliseconds");

    // The objective value of the solution.
    Console.WriteLine("Optimal objective value = " +
                       solver.ObjectiveValue());

    // The value of each variable in the solution.
    Console.WriteLine("x1 = " + x1.SolutionValue());
    Console.WriteLine("x2 = " + x2.SolutionValue());

    Console.WriteLine("Advanced usage:");
    Console.WriteLine("Problem solved in " + solver.Nodes() +
                       " branch-and-bound nodes");
  }

  static void Main()
  {
    Console.WriteLine("---- Integer programming example with GLPK ----");
    RunIntegerProgrammingExample("GLPK_MIXED_INTEGER_PROGRAMMING");
    Console.WriteLine("---- Linear programming example with CBC ----");
    RunIntegerProgrammingExample("CBC_MIXED_INTEGER_PROGRAMMING");
    Console.WriteLine("---- Linear programming example with SCIP ----");
    RunIntegerProgrammingExample("SCIP_MIXED_INTEGER_PROGRAMMING");
  }
}
