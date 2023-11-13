% Python virtual environment activation command
activateCommand = 'C:\Users\HPRVa\Ballistic_shield_design_optimization\Scripts\activate'; % For Windows

% Path to the Python interpreter within the virtual environment
pythonInterpreter = 'C:\Users\HPRVa\Ballistic_shield_design_optimization\Scripts\python.exe'; % Replace with your interpreter path

% Path to the Python file
% pythonFile = 'C:\Users\HPRVa\Ballistic_shield_design_optimization\src\helloworld.py';

% Specify the path to the folder containing your Python script
% if count(py.sys.path,pwd) == 0
%     insert(py.sys.path,int32(0),pwd);
% end

camxy = @(x,y) x^2 + y^2;

x = optimvar("x","LowerBound",4,"UpperBound",10);
y = optimvar("y","LowerBound",3,"UpperBound",9);

cam = camxy(x,y);

prob = optimproblem("Objective",cam);

show(prob)

options = optimoptions(@ga,'Display','iter');

[sol,fval] = solve(prob,"Solver","ga","Options",options)

% Display the best parameters and minimized function value
disp('Best Parameters:');
disp(sol);
disp('Minimized Function Value:');
disp(fval);