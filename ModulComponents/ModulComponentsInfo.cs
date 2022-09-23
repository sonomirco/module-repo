using Grasshopper;
using Grasshopper.Kernel;
using System;
using System.Drawing;

namespace ModulComponents
{
    public class ModulComponentsInfo : GH_AssemblyInfo
    {
        public override string Name => "ModulComponents";

        //Return a 24x24 pixel bitmap to represent this GHA library.
        public override Bitmap Icon => null;

        //Return a short string describing the purpose of this GHA library.
        public override string Description => "";

        public override Guid Id => new Guid("380879E6-EA27-4681-AD56-59CF2C76A19B");

        //Return a string identifying you or your company.
        public override string AuthorName => "";

        //Return a string representing your preferred contact details.
        public override string AuthorContact => "";
    }
}